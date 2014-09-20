// Generated by CoffeeScript 1.6.3
var side_chart;

window.fake_side_data = function() {
  var last, _i, _results;
  last = Math.random() * 100;
  return (function() {
    _results = [];
    for (_i = 0; _i < 200; _i++){ _results.push(_i); }
    return _results;
  }).apply(this).map(function(i) {
    return {
      close: parseInt(last + (Math.random() * 10) - 20),
      date: d3.time.format("%d").parse("" + i)
    };
  });
};

side_chart = function(sel) {
  var color;
  if (sel == null) {
    sel = "body";
  }
  color = "rgb(96,61,105)";
  return $(sel).oj(div({
    style: "height:100px; width:100%;"
  }, function() {
    div({
      style: "position:absolute; display:block; left:-9px; text-align:left; top:8px; font-size:16px; color:grey;"
    }, function() {
      div(function() {
        return " -2." + (parseInt(Math.random() * 9)) + "%";
      });
      return div({
        style: "font-size:13px; color:lightgrey; top:13px;"
      }, function() {
        return "3 hours ago";
      });
    });
    div({
      style: "position:absolute; display:block; left:" + (Math.random() * 200) + "px; top:13px; height:24px; width:" + 5 + "px; border-radius:2px; background-color:darkseagreen;  -ms-transform: rotate(19deg); -webkit-transform: rotate(19deg); transform: rotate(19deg); "
    });
    div({
      style: "position:absolute; display:block; left:180px; text-align:left; top:9px; font-size:16px; color:grey;"
    }, function() {
      div(function() {
        return "2." + (parseInt(Math.random() * 9)) + "%";
      });
      return div({
        style: " top:-30px; line-height:80%; font-size:13px; width:70px; left:-20px; color:lightgrey; width:50px; top:14px;"
      }, function() {
        return "1 hour ago";
      });
    });
    return div({
      style: "position:absolute; display:block; left:0px; top:27px; height:1px; width:" + 200 + "px; background-color:rgb(31,71,103);;"
    });
  }));
};

/*
//@ sourceMappingURL=side_chart.map
*/
