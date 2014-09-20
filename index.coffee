arr= [
  "./libs/jquery.js",
  "./libs/sugar.js",
  "./libs/oj.js",
  "./libs/easings.js",
  "./libs/dirty.js",
  "./libs/d3.js",
  "./libs/colour.js",
  "./coffeejs/webcam.js",
  "./coffeejs/line_chart.js",
]
head.js.apply(this, arr);

head ->
  oj.useGlobally();

  make_fact= ()->
    value= 234.04
    title= "New York Times"
    time= "3 minutes ago"
    cents= (value - parseInt(value)).toFixed(2);
    cents= cents.replace(/^0\./,'')
    html= """
      <div id="infact" style="width:100%; text-align:center; height:#{200}px; position:relative;">
        <span style="position:absolute; display:inline-block; top:5px; left:5px; font-size:22px; color:steelblue;">#{title}</span>

        <span style="position:relative; top: 25px; display:inline-block; font-size:180px; color:slategrey;">#{parseInt(value)}</span>
        <span style="position:relative; top:-45px; display:inline-block; font-size:50px; color:darkseagreen;">.#{cents}</span>
        <span style="position:relative; top:55px; left:-75px; display:inline-block; font-size:20px; color:#{colourscheme.bluebrowns(0.8)};">#{time}</span>
        <svg id="chart" style="position:relative; display:block; left:25px; height:100px; width:80%;"></svg>
      </div>
    """
    $("#fact_pane").html(html)
    line_chart("#chart")

  state= 0
  change_state=()->
    if state==0
      make_fact()
      $("#fact_pane").animate {height:"50%"}, {duration:500, easing:"easeOutExpo"}
      state= 1
    else
      $("#fact_pane").animate {height:"18%"}, {duration:500, easing:"easeOutExpo"}
      state= 0


  $("body").oj(
    div {
      style:"position:relative; display:block; width:100%; height:680px; border:1px solid grey;"
      },->
        div {
          id:"video_pane"
          style:"position:relative;  display:block; width:100%; height:80%; overflow:hidden; border:10px solid #{colourscheme.bluebrowns(0.6)}; border-radius:5px;"
          insert:->
            video= """
                <div id="canvasHolder" style="display:none;"></div>
                <video id="video" style="position:absolute; top:0px; cursor:pointer; width:100%; height:400px; " src=""></video>
              """
            $(this).ojAppend(video)
            window.webcam("canvasHolder", send_to_patrick)
          },->
        div {
          id:"fact_pane"
          style:"position:absolute; bottom:0px; background-color:white; z-index:2; width:100%; height:18%; overflow:hidden; border:10px solid #{colourscheme.bluebrowns(0.6)};"
          click:-> change_state()
          },->



    )

  send_to_patrick=(data)->
    alert(data)
