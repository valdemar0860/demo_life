$(document).ready(function() {
    $("#input_field").on("input", function() {
        var input_data = $(this).val();
  
        $.ajax({
            url: "/autosave/",
            type: "POST",
            data: {
                input_data: input_data
            },
            success: function(response) {
                console.log("Data saved successfully!");
            }
        });
    });
});