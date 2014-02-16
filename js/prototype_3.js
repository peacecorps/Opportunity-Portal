function Prototype3Ctrl($scope, $http){
    $scope.data = {};
    $scope.state = {};
    $scope.state.sectors = ['Business', 'Environment'];
    $scope.state.regions = ['South Africa'];
    $scope.state.countries = ['Ethiopia', 'Kenya'];

    $http({
        url: "http://idhack.iis-dev.seas.harvard.edu/get_jobs" ,
        method: "GET",
        params: {location: "Ghana"}
    }).success(function(data){
        $scope.data.jobs = data.data;
        $scope.data.currJob = data.data[0];
        updateStat();
        $scope.data.jobs[0].selected = true;

        // alert(data.data[0]['title']);
    });
    var updateStat = function(){
        for (var i = 0; i < $scope.data.jobs.length; i++){
            $scope.data.jobs[i].rural = (Math.random() > 0.2);
            $scope.data.jobs[i].hot = (Math.random() > 0.5);
            $scope.data.jobs[i].cold = (Math.random() > 0.5);

        }


    };

    $scope.toggleSector = function(sect){
        var sIdx = $scope.state.sectors.indexOf(sect)
        if( sIdx == -1){
            $scope.state.sectors.push(sect);
        }else{
            $scope.state.sectors.splice(sIdx,1);
        }
        $scope.getJobs();
    };

    $scope.toggleCountry = function(sect){
        var sIdx = $scope.state.countries.indexOf(sect)
        if( sIdx == -1){
            $scope.state.countries.push(sect);
        }else{
            $scope.state.countries.splice(sIdx,1);
        }
        $scope.getJobs();
    };

    $scope.toggleRegion = function(reg){
        var sIdx = $scope.state.regions.indexOf(reg);
        if( sIdx == -1){
            $scope.state.regions.push(reg);
        }else{
            $scope.state.regions.splice(sIdx,1);
        }
        // $scope.getJobs();
    };

    $scope.getJobs = function(){
        console.log($scope.state.regions);
        $http({
            url: "http://idhack.iis-dev.seas.harvard.edu/get_jobs" ,
            method: "GET",
            params: {sector: $scope.state.sectors.join("+"),
                     location: $scope.state.countries.join("+")}
        }).success(function(data){
            $scope.data.jobs = null;
            $scope.data.jobs = data.data;
            updateStat();
            // alert(data.data[0]['title']);
        }).error(function(data, status, headers, config) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
            console.log(status);
        });;
    };

    $scope.selectJob = function(aa){
        for(var i = 0; i < $scope.data.jobs.length; i++){
            if(aa == $scope.data.jobs[i].AA){
                $scope.data.currJob = $scope.data.jobs[i];
                console.log($scope.data.jobs[i]);
                geocoder.query(String($scope.data.jobs[i].location), showMap);
                
                break;
            }
        }
        
    };
}
function showMap(err, data) {
             map.fitBounds(data.lbounds);
        }
