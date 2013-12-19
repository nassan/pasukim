'use strict';

/* Controllers */

// var pasukimApp = angular.module('pasukimApp', []);

// pasukimApp.controller('pasukimListControl', function($scope, $http) {
//   $http.get('/pasukim.json').success(function(pasukimFromJSON) {
//     $scope.pasukim = pasukimFromJSON;
//   });
// });
function pasukimListController($scope,$http)
{
	$http.get('perek1.json').success(function(pasukimFromJSON)
	{
		$scope.pasukim = pasukimFromJSON;
		
	});
	// };
	// $scope.testString = 'בראשית ברא אלהים את השמים ואת הארץ';
}
