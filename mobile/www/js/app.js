// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
var app = angular.module('starter', [
  'ngRoute',
  'ionic',
  'controllers'
]);

// , function($httpProvider){

//  // Use x-www-form-urlencoded Content-Type
//   $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

//   /**
//    * The workhorse; converts an object to x-www-form-urlencoded serialization.
//    * @param {Object} obj
//    * @return {String}
//    */
//   var param = function(obj) {
//     var query = '', name, value, fullSubName, subName, subValue, innerObj, i;

//     for(name in obj) {
//       value = obj[name];

//       if(value instanceof Array) {
//         for(i=0; i<value.length; ++i) {
//           subValue = value[i];
//           fullSubName = name + '[' + i + ']';
//           innerObj = {};
//           innerObj[fullSubName] = subValue;
//           query += param(innerObj) + '&';
//         }
//       }
//       else if(value instanceof Object) {
//         for(subName in value) {
//           subValue = value[subName];
//           fullSubName = name + '[' + subName + ']';
//           innerObj = {};
//           innerObj[fullSubName] = subValue;
//           query += param(innerObj) + '&';
//         }
//       }
//       else if(value !== undefined && value !== null)
//         query += encodeURIComponent(name) + '=' + encodeURIComponent(value) + '&';
//     }

//     return query.length ? query.substr(0, query.length - 1) : query;
//   };

//   // Override $http service's default transformRequest
//   $httpProvider.defaults.transformRequest = [function(data) {
//     return angular.isObject(data) && String(data) !== '[object File]' ? param(data) : data;
//   }];
// });

app.config(['$routeProvider',
            function($routeProvider) {
              $routeProvider.
                when('/', {
                  templateUrl: 'index.html',
                  controller: 'IndexCtrl'
                })
            }]);
app.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if(window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }

    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
});