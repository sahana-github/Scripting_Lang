window.onload = function() {

    var teslaModels = [
        {
            "model": "modelS",
            "name": "Model S",
            "price": 69200,
            "year": 2016
        },
        {
            "model": "modelX",
            "name": "Model X",
            "price": 83700,
            "year": 2017
        },
        {
            "model": "model3",
            "name": "Model 3",
            "price": 35000,
            "year": 2017
        },
    ];

    //Generate HTML for Menu Bar
    teslaModels.forEach(function(item,index){
        listElemet = document.createElement("th")
        listElemet.id = item.model
        listElemet.innerHTML = item.name
        document.getElementById("menu").appendChild(listElemet)
    })

    // add event handler for mouseover on each img:
    teslaModels.forEach(mouseOverHandler);
    function mouseOverHandler(item, index)
    {
        var elem = document.getElementById(item.model);
        elem.onmouseover = function(){
             var details = item;
            // if found, update DOM with information from array
            if(details!=null)
            {
                document.getElementById("data-table").removeAttribute('hidden');
                document.getElementById("model").innerHTML = details.name;
                document.getElementById("picture").innerHTML = '<img src="'+details.model+'.jpeg"/>';
                document.getElementById("price").innerHTML = "$"+details.price;
                document.getElementById("year").innerHTML = details.year;

            }
        }
    }


};
