
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    let options = {};
    var instances = M.Modal.init(elems, options);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.modal').modal();
  });



$(".modal-close").click(function(){
let pid = $(this).attr('id');
let remail = $('#remail').val();
sendProductMail(pid,remail)
});


 function sendProductMail(pid,remail) {
    console.log("fetching python localhost");
    let url = "http://127.0.0.1:5000/send-mail/"+ pid + "/" + remail;
   fetch(url)
  .then((resp) => resp.json()) // Transform the data into json
  .then(function(data) {
   console.log(data);
    })

  }