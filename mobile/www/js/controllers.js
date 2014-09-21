var controllers = angular.module('controllers', []);

function onSuccess () {
  alert("woo");
}

function onFail(msg) {
  alert("failed because: " + msg);
}

function getPhotoForType(type) {
  var photo = navigator.camera.getPicture(onSuccess, onFail, {
    quality: 100,
    destinationType: Camera.DestinationType.FILE_URI,
    sourceType: type
  });

  console.log("got photo: " + photo);
  return photo;
}

function uploadPhoto() {
  return getPhotoForType(Camera.PictureSourceType.PHOTOLIBRARY);
}

function takePhoto() {
  return getPhotoForType(Camera.PictureSourceType.CAMERA);
}

controllers.controller("IndexCtrl", [
  '$scope',
  function($scope) {
    $scope.uploadPhoto = uploadPhoto;
    $scope.takePhoto = takePhoto;
  }
]);
