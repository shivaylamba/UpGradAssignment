
 let searchKeyword = "";

 $(document).ready(function(){
  $('#autocomplete-input').on('input',function(e){
    searchKeyword = $(this).val()
     fetchDat();
    console.log($(this).val())
     });

  });

 function fetchDat() {
    console.log("fetching python localhost");
    let url = "http://127.0.0.1:5000/search/"
   fetch(url+searchKeyword)
  .then((resp) => resp.json()) // Transform the data into json
  .then(function(data) {
console.log(data);

   const searchObjectindex = arrayToObjectIndex(data)


   const searchObject = arrayToObject(data)
//console.log(searchObject);

  $('#autocomplete-input').autocomplete({
      data:  searchObject,
      limit: 4,
       onAutocomplete: function(name) {
          console.log(name);
        let  id = searchObjectindex[name];
        window.location.href = "http://127.0.0.1:5000/product/"+id;
        },
    });


    })
  }


const arrayToObject = (array) =>
   array.reduce((obj, item) => {
     obj[item.name] = item.image
     return obj
   }, {})


   const arrayToObjectIndex = (array) =>
   array.reduce((obj, item) => {
     obj[item.name] = item.id
     return obj
   }, {})


$('img').click(function() {
    let pid = $(this).attr('id');
    console.log(pid);
    window.location.href = "http://127.0.0.1:5000/product/"+pid;
    return false;
});