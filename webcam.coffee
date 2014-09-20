
window.webcam= (id="canvasHolder", cb=->)->


  connect = (stream) ->
    video = document.getElementById("video")
    video.src = (if window.URL then window.URL.createObjectURL(stream) else stream)
    video.play()
  error = (e) ->
    console.log e
  captureImage = ->
    video = document.getElementById("video")
    canvas = document.createElement("canvas")
    canvas.id = "hiddenCanvas"

    #add canvas to the body element
    document.body.appendChild canvas

    #add canvas to #canvasHolder
    document.getElementById(id).appendChild canvas
    ctx = canvas.getContext("2d")
    canvas.width= 500
    canvas.height= 500
    ctx.drawImage video, 0, 0, 500, 500

    #save canvas image as data url
    dataURL = canvas.toDataURL()
    console.log dataURL
    cb(dataURL)

  navigator.myGetMedia = (navigator.getUserMedia or navigator.webkitGetUserMedia or navigator.mozGetUserMedia or navigator.msGetUserMedia)
  navigator.myGetMedia
    video: true
  , connect, error

  #Bind a click to a button to capture an image from the video stream
  el = document.getElementById("video")
  el.addEventListener "click", captureImage, false
