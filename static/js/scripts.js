$(function() {
   $('.img').on('click', function() {
      $('.imagepreview').attr('src', $(this).find('img').attr('src'));
      $('#imagemodal').modal('show');   
   });		
});

var modalDiv = $("#modal-div");

$(".open-modal").on("click", function() {
  $.ajax({
    url: $(this).attr("data-url"),
    success: function(data) {
      modalDiv.html(data);
      $("#myEdit").modal();
    }
  });
});