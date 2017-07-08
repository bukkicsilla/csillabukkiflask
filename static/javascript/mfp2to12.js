$(document).ready(function(){
    
    $(".mmm").html(function(){
          //numbers 2 -> 12; first number = how many numbers, second number = starting number
          var a = Math.floor((Math.random() * 11) + 2);
          var b = Math.floor((Math.random() * 11) + 2);
          return "<p class='mfp'>" + a + " x " + b + " = </p>";
        });
});
