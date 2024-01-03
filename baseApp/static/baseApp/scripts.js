$(document).ready(() => {
  

  //GLOBAL VARIABLES
  var cart_storage = JSON.parse(localStorage.getItem("cart"));
  var cart_items_json = document.getElementById("cart_items_json");

  
  //FUNCTIONS TO LOAD ON FIRST RENDER
  cart_items_json.value = JSON.stringify(cart_storage)


  




  

  //Main Logo Animation
  $("#MainLogo").mouseover(() => {
    $("#MainLogo").css("color", "#ef7710");
  });
  $("#MainLogo").mouseleave(() => {
    $("#MainLogo").css("color", "#352");
  });

  $(".log-form").slideDown();
  //Sign logo
  $(".sign-legend").animate(
    {
      opacity: "1",
      fontSize: "50px",
    },
    1500
  );

  //pizza animation
  $(".pizza-vector").animate(
    {
      opacity: "1",
      // width:'28%'
    },
    1800
  );

  $(".menu-heading").animate(
    {
      opacity: "1",
      fontSize: "50px",
    },
    1500
  );
  $(".menu").animate(
    {
      opacity: "1",
    },
    1500
  );

  $(".about-heading").animate(
    {
      opacity: "1",
      fontSize: "40px",
    },
    1500
  );

  $(".about-para").animate(
    {
      opacity: "1",
    },
    1500
  );
  //social logo animations

  
  //adding item to cart
  var addToCart = (id) => {
    if (localStorage.getItem("cart")) {
      var cart = JSON.parse(localStorage.getItem("cart"));
      cart[id] = 1;
      localStorage.setItem("cart", JSON.stringify(cart));
    } else {
      var cart = {};
      cart[id] = 1;
      localStorage.setItem("cart", JSON.stringify(cart));
    }

    $("#cart_items_json").val(localStorage.getItem("cart"))

   


  };

  //removing item from cart
  var removefromCart = (id) => {
    var cart_local = JSON.parse(localStorage.getItem("cart"));
    delete cart_local[id];
    localStorage.setItem("cart", JSON.stringify(cart_local));

    
    cart_items_json.value = JSON.stringify(cart_local);

    $("#cart_items_json").val(localStorage.getItem("cart"))

    
  };

  //functions that change the state of the buttons based on items in local storage

  // adding product cart
  $(".buy-btn").on("click", function () {
    let prod_id = $(this).attr("id");
    addToCart(prod_id);

    //adding styles on buy-button click
    $(this).text("Added");
    $(this).parent().children(".remove-btn").css("display", "inline");
    // Add a class to change the button color
    $(this).removeClass("btn-success-light");
    $(this).addClass("btn-success");
    $(this).addClass("added");
    //updating the cart
    
  });

  $(".remove-btn").on("click", function () {
    var btn_id = $(this).parent().children(".buy-btn").attr("id");
    $(this).parent().children(".buy-btn").text("Add to cart");
    $(this).parent().children(".buy-btn").removeClass("btn-success");
    $(this).parent().children(".buy-btn").addClass("btn-success-light");

    $(this).css("display", "none");
    let prod_id = $(this).parent().children(".buy-btn").attr("id");

    removefromCart(prod_id);
  });

    




  // change the state of add to cart buttons to added
  
  
});
