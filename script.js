function DisplaySTORY(noun1,noun2,noun3,noun4,noun5,noun6,noun7) {
    var poem = "Be kind to your " + noun1 + " -footed " + noun2 + " For a duck may be somebody`s " + noun3 + " Be kind to your " + noun4 + " in " + noun5 +  " Where the weather is always " + noun6 + ". You may think that this is the " + noun7 + ", Well it is. ";
    $('#output').html(poem);
}

$('#noun').click(function(){
    var passThis1 = $('input[name="noun1"]').val();
    var passThis2 = $('input[name="noun2"]').val();
    var passThis3 = $('input[name="noun3"]').val();
    var passThis4 = $('input[name="noun4"]').val();
    var passThis5 = $('input[name="noun5"]').val();
    var passThis6 = $('input[name="noun6"]').val();
    var passThis7 = $('input[name="noun7"]').val();

    DisplaySTORY(passThis1,passThis2,passThis3,passThis4,passThis5,passThis6,passThis7);
});
