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
  window.my_width= 280
  window.my_height= 493

  make_fact= ()->
    value= 234.04
    title= "New York Times"
    time= "3 minutes ago"
    cents= (value - parseInt(value)).toFixed(2);
    cents= cents.replace(/^0\./,'')
    html= """
      <div id="infact" style="width:100%; text-align:center; height:#{200}px; position:relative;">
        <span style="position:absolute; display:inline-block; top:5px; left:5px; font-size:22px; color:steelblue;">#{title}</span>
        <span style="position:absolute; top:45px; left:5px; font-size:42px; color:steelblue;">$</span>

        <span style="position:relative; top: 25px; display:inline-block; font-size:180px; color:slategrey;">#{parseInt(value)}</span>
        <span style="position:relative; top:-45px; display:inline-block; left:50px; font-size:50px; color:darkseagreen;">.#{cents}</span>
        <span style="position:relative; top:55px; left:-75px; display:inline-block; font-size:20px; color:steelblue;">#{time}</span>
        <svg id="chart" style="position:relative; display:block; left:25px; height:100px; width:80%;"></svg>
      </div>
    """
    $("#fact_pane").html(html)
    line_chart("#chart")

  state= 0
  change_state=()->
    $("#by_image").html('')
    if state==0
      make_fact()
      $("#fact_pane").animate {height:"80%"}, {duration:500, easing:"easeOutExpo"}
      state= 1
    else
      $("#fact_pane").animate {height:"25%"}, {duration:500, easing:"easeOutExpo"}
      state= 0

  device=(ojarr=[])->
    $("body").oj(
      div {
        style:"position:absolute; display:block; width:700px; background-repeat:no-repeat; height:700px; background-image:url(./frame.svg);"
      },->
        div {
          style:"position:absolute; overflow:none; display:block; left:30px; top: 106px; width:#{window.my_width}px; height:#{window.my_height}px; background-color:white;"
        },->
          ojarr


    )


  main_frame=->
    div {
      style:"position:relative; display:block; overflow:hidden; width:#{window.my_width}px; height:#{window.my_height}px; border:1px solid grey;"
      },->
        div {
          id:"video_pane"
          style:"position:relative;  display:block; width:100%; height:80%;  border-radius:5px;"
          insert:->
            video= """
                <div id="canvasHolder" style="display:none;"></div>
                <video id="video" style="position:absolute; top:0px; cursor:pointer; width:#{window.my_width+200}px; height:#{window.my_height-125}px; " src=""></video>
              """
            $(this).ojAppend(video)
            window.webcam("canvasHolder", (data)->send_to_patrick(data))
            message= """
              <span id="by_image" style="position:absolute; text-align:left; z-index:1; left:20px; top: 25px; display:inline-block; font-size:100px; color:steelblue;">
                search by image
              </span>
            """
            # $(this).append(message)
          },->
        div {
          id:"fact_pane"
          style:"position:absolute; bottom:0px; background-color:white; z-index:2; width:100%; height:25%; overflow:hidden; border-top:10px solid steelblue;"
          click:-> change_state()
          },->
            span {
              style:"color:steelblue; position:relative; left:25px; top:35px; font-size:24px;"
            },->
              "Insight into a company"

      #cross
        div {
          style:"position:absolute; display:block; left:50%; top:0px; width:1px; height:#{window.my_height}px; background-color:black;"
        }
        div {
          style:"position:absolute; display:block; left:0%; top:50%; height:1px; width:#{window.my_width}px; background-color:black;"
        }
  send_to_patrick=(data)->
    # alert(data)
    change_state()

  device(main_frame())
