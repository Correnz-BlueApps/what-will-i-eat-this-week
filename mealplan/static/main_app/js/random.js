const chefkoch = require('chefkoch-api');

chefkoch.chefkochAPI.getRecipe('/rezepte/1127371219159420/Dinkel-Hirse-Vollkornbrot.html'/*this is the subURL of the recipe*/).then(function(data){
    console.log(data);
});