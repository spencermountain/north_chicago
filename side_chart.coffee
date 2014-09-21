window.fake_side_data= ->
  last= Math.random()*100
  [0...200].map (i)->
    {
      close: parseInt(last + (Math.random() *10)-20),
      date: d3.time.format("%d").parse("#{i}")
    }


side_chart= (sel="body")->
  color= "rgb(96,61,105)"
  $(sel).oj(
    div {style:"height:100px; width:100%;"},->

      #left text
      div {
        style:"position:absolute; display:block; left:-9px; text-align:left; top:8px; font-size:16px; color:grey;"
      }, ->
        div -> " -2.#{parseInt(Math.random()*9)}%"
        div {style:"font-size:13px; color:lightgrey; top:13px;"},-> "3 hours ago"


      #middle
      div {
        style:"position:absolute; display:block; left:#{Math.random()*200}px; top:13px; height:24px; width:#{5}px; border-radius:2px; background-color:darkseagreen;  -ms-transform: rotate(19deg); -webkit-transform: rotate(19deg); transform: rotate(19deg); "
      }
      #left text
      div {
        style:"position:absolute; display:block; left:180px; text-align:left; top:9px; font-size:16px; color:grey;"
      }, ->
        div -> "2.#{parseInt(Math.random()*9)}%"
        div {style:" top:-30px; line-height:80%; font-size:13px; width:70px; left:-20px; color:lightgrey; width:50px; top:14px;"},-> "1 hour ago"


      #axis
      div {
        style:"position:absolute; display:block; left:0px; top:27px; height:1px; width:#{200}px; background-color:rgb(31,71,103);;"
      }
  )