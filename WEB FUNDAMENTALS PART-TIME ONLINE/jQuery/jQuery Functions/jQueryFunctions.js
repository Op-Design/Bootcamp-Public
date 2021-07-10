$(document).ready(function(){
    console.log("Hello World");
    $('#click').click(function(){
        alert("You clicked the .click button!");
    })
    $('#hide').click(function(){
        alert("You clicked the .hide button!");
        $('.hideshow p').hide();
    })
    $('#show').click(function(){
        alert("You clicked the .show button!");
        $('.hideshow p').show();
    })
    $('#toggle').click(function(){
        alert("You clicked the .toggle button!");
        $('.hideshow p').toggle();
    })
    $('#slideDown').click(function(){
        alert("You clicked the .slideDown button!");
        $('.slide p').slideDown();
    })
    $('#slideUp').click(function(){
        alert("You clicked the .slideUp button!");
        $('.slide p').slideUp();
    })
    $('#slideToggle').click(function(){
        alert("You clicked the .slideToggle button!");
        $('.slide p').slideToggle();
    })
    $('#fadeIn').click(function(){
        alert("You clicked the .fadeIn button!");
        $('.fade p').fadeIn();
    })
    $('#fadeOut').click(function(){
        alert("You clicked the .fadeOut button!");
        $('.fade p').fadeOut();
    })
    $('#addClass').click(function(){
        alert("You clicked the .addClass button!");
        $('.fade p').addClass("slide");
    })
    $('#removeClass').click(function(){
        alert("You clicked the .removeClass button!");
        $('.fade p').removeClass("slide");
    })
    $('#before').click(function(){
        alert("You clicked the .before button!");
        $('.append p').before('before');
    })
    $('#after').click(function(){
        alert("You clicked the .after button!");
        $('.append p').after('after');
    })
    $('#append').click(function(){
        alert("You clicked the .append button!");
        $('.append p').append('append');
    })
})