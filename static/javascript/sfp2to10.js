$(document).ready(function(){
    
    $(".mmm").html(function(){
          //numbers 2 -> 10; first number = how many numbers, second number = starting number
          var a = Math.floor((Math.random() * 9) + 2);
          var b = Math.floor((Math.random() * 9) + 2);
          var c = a+b;
          return "<p class='mfp'>" + c + " - " + a + " = </p>";
        });
});
