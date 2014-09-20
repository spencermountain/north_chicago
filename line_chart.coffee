line_chart= (sel="body")->
  margin =
    top: 20
    right: 20
    bottom: 30
    left: 50

  width = window.screen.availWidth - margin.left - margin.right
  height = 150 - margin.top - margin.bottom
  parseDate = d3.time.format("%d-%b-%y").parse
  x = d3.time.scale().range([0, width])
  y = d3.scale.linear().range([height, 0])
  xAxis = d3.svg.axis().scale(x).orient("bottom")
  yAxis = d3.svg.axis().scale(y).orient("left")
  line = d3.svg.line().x((d) ->
    x d.date
  ).y((d) ->
    y d.close
  )
  svg = d3.select(sel).attr("width", width ).attr("height", height).append("g")
  d3.tsv "data.tsv", (error, data) ->
    data.forEach (d) ->
      d.date = parseDate(d.date)
      d.close = +d.close

    x.domain d3.extent(data, (d) ->
      d.date
    )
    y.domain d3.extent(data, (d) ->
      d.close
    )
    svg.append("path").datum(data).attr("class", "line").attr "d", line

  svg.append("g").attr("class", "x axis").attr("transform", "translate(0," + height + ")").call xAxis
