"use strict";
document.addEventListener("DOMContentLoaded", function(e) {
    let money=0;
    let level = 0;
    let timeToComplete=1000;
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
    let value = Number(levelsInfo[level].commuter.money);


    let tollProfit = setInterval(addMoney, timeToComplete);
    function addMoney(){
        money += value
        document.getElementById("money").textContent = "Money: " + money + "$"
    }


    for (let upgrade of document.getElementsByClassName("upgrade")){
        let cost = document.createElement("h3")
        cost.textContent = value;
        upgrade.append(cost)
    }

    // handle all options
    document.addEventListener("click", function(e){
        if (e.target.classList.contains("upgrade")){
            if (e.target.id === "addition"){
                addition += value
            } else if (e.target.id === "timeToComplete"){
                timeToComplete -= value
            } else if(e.target.id === "addition"){
                addition += value
            } else if(e.target.id === "levelUpgrade"){
                window.location.href = '/character'
            } 
        }
        clearInterval(tollProfit)
        tollProfit = setInterval(addMoney, timeToComplete);
    })

    
});