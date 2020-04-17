const app = angular.module('app', []);


app.controller('mainCtrl', ['$scope', '$http', function($scope, $http, $filter) {

	//Code to make new window
	const BrowserWindow = require('electron').remote.BrowserWindow;
	const path = require('path');
	const url = require('url');

	courseMap = new Map();
	$scope.currentInput=""; // Sets default input to empty
	let idCount = 0;

	$scope.addCourse = function() {

		let toAdd = $scope.currentInput;
		let isValid = validateCourse(toAdd);

		if (isValid) {
			courseMap.set(idCount,{
				id: idCount,
				name:toAdd
			});
			$scope.currentInput=""; // Sets it backed to empty
		}
		idCount++;
	}

	$scope.getCourseVals = function() {
		return Array.from(courseMap.values());
	}


	$scope.removeCourse = function(id) {
		courseMap.delete(id);
	}


	function validateCourse (course) {

		if (course.length === 8) {
			return /[A-Z]{4}\s[0-9]{3}/.test(course);
		} else {
			return false;
		}
		
	}



}]);