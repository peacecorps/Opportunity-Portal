function Prototype3Ctrl($scope, $http){
    $scope.data = {};
    $scope.state = {};
    $scope.state.sectors = [];


    $http({
        url: "http://idhack.iis-dev.seas.harvard.edu/get_jobs" ,
        method: "GET",
        params: {location: "Ghana"}
    }).success(function(data){
        $scope.data.jobs = data.data;
        $scope.data.currJob = data.data[0];
        $scope.data.jobs[0].selected = true;
        // alert(data.data[0]['title']);
    });

    $scope.toggleSector = function(sect){
        var sIdx = $scope.state.sectors.indexOf(sect)
        if( sIdx == -1){
            $scope.state.sectors.push(sect);
        }else{
            $scope.state.sectors.splice(sIdx,1);
        }
        $scope.getJobs();
    };

    $scope.getJobs = function(){
        console.log($scope.state.sectors);
        $http({
            url: "http://idhack.iis-dev.seas.harvard.edu/get_jobs" ,
            method: "GET",
            params: {sector: $scope.state.sectors.join("+")}
        }).success(function(data){
            $scope.data.jobs = data.data;
            // alert(data.data[0]['title']);
        }).error(function(data, status, headers, config) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
            console.log(status);
        });;
    };
}