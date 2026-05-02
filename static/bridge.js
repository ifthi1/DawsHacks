"use strict";
document.addEventListener("DOMContentLoaded", function(e) {
    let money=0;
    let level = 0;
    let timeToComplete=5000;
    let multiplier=1;
    let addition=0;
    const menu = document.getElementById("menu");
    let levelsInfo = [
        {
            "bridge": "wood",
            "commuter": {
                "type": "person",
                "money":  "1"
            }
            
        },
        {
            "bridge": "stone",
            "commuter": {
                "type": "carriage",
                "money":  "5"
            }
            
        },
        {
            "bridge": "iron",
            "commuter": {
                "type": "bike",
                "money":  "10"
            }
            
        },
        {
            "bridge": "steel",
            "commuter": {
                "type": "car",
                "money":  "25"
            }
            
        },
        {
            "bridge": "illuminate bar",
            "commuter": {
                "type": "bus",
                "money":  "50"
            }
            
        }

    ]

    // handle all options
    document.addEventListener("click", function(e){
        if (e.target.classList.contains("upgrade")){
            
        }
    })

    let tollProfit = setInterval(addMoney, timeToComplete);
    function addMoney(){
        money += Number(levelsInfo[level].commuter.money)
        document.getElementById("money").textContent = "Money: " + money + "$"
    }
});