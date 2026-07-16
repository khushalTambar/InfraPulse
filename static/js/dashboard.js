const ctx = document.getElementById("cpuChart");

if(ctx){

new Chart(ctx,{

type:"line",

data:{

labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],

datasets:[{

label:"CPU Usage",

data:[20,35,28,45,55,42,34],

borderColor:"#3b82f6",

backgroundColor:"rgba(59,130,246,.2)",

fill:true,

tension:.4

}]

},

options:{

plugins:{

legend:{

labels:{

color:"white"

}

}

},

scales:{

x:{

ticks:{color:"white"}

},

y:{

ticks:{color:"white"}

}

}

}

});

}