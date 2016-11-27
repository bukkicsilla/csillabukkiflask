$(document).ready(function(){
    //$("p").click(function(){
        //$(this).hide();
        //alert("Text: " + $(".mfp").text());
    //});
    //$(".mfp").text("5 x 5 = ");
    //$(".mmm").html("<p class='mfp'> 8 x 9 = </p>");
    $(".mmm").html(function(){
          //numbers 2 -> 10; first number = how many numbers, second number = starting number
          var a = Math.floor((Math.random() * 11) + 2);
          var b = Math.floor((Math.random() * 11) + 2);
          return "<p class='mfp'>" + a + " x " + b + " = </p>";
        });
});
