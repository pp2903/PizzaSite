$(document).ready(() => {
  //page loads with fading animation
  // $('body').css('display', 'none');
  // $('body').fadeIn(2000);

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

  var cart = localStorage.getItem("cart");
  if (cart === null) {
    localStorage.setItem("cart", JSON.stringify({}));
  }
  //adding item to cart
  var addToCart = (id) => {
    if (localStorage.getItem("cart")) {
      var cart = JSON.parse(localStorage.getItem("cart"));
      cart[id] = true;
      localStorage.setItem("cart", JSON.stringify(cart));
    } else {
      var cart = {};
      cart[id] = true;
      console.log(cart);
      localStorage.setItem("cart", JSON.stringify(cart));
    }
  };

  //removing item from cart
  var removeProd = (id) => {
    var cart = JSON.parse(localStorage.getItem("cart"));

    cart[id] = false;
    console.log(cart);
    localStorage.setItem(JSON.stringify(cart));
  };

  //functions that change the state of the buttons based on items in local storage
  var cart = [] //global variable that stores the cart value that is sent to the server

  var updateCart = (id,action) =>{
    
    if(action==="add"){
      cart.push(id)
      console.log(cart)
    }

    if(action==="del"){
      cart = cart.filter((prod_id)=> prod_id!==id)
      console.log(cart)
    }    
    
    $('#cart_items_json').val(JSON.stringify(cart))
    console.log(JSON.stringify(cart))


  }








  // adding product cart
  $(".buy-btn").on("click", function () {
    var btn_id = $(this).attr("id");
    addToCart(btn_id);
    $(this).text("Added");

    $(this).parent().children(".remove-btn").css("display", "inline");

    // Add a class to change the button color
    $(this).removeClass("btn-success");
    $(this).addClass("btn-primary");
    $(this).addClass("added");
    //updating the cart

    updateCart(btn_id,"add")



  });

  $(".remove-btn").on("click", function () {

    var btn_id = $(this).parent().children(".buy-btn").attr('id')
    $(this).parent().children(".buy-btn").text("Add to cart");
    $(this).parent().children(".buy-btn").removeClass("btn-primary");
    $(this).parent().children(".buy-btn").addClass("btn-success");

    $(this).css("display", "none");
    console.log($(this).parent().children(".buy-btn").attr("id"));
    var prod_id = $(this).parent().children(".buy-btn").attr("id");

    var cart = JSON.parse(localStorage.getItem("cart"));
    cart[prod_id] = false;
    localStorage.setItem("cart", JSON.stringify(cart));

    // updating the cart

    updateCart(btn_id,"del")


  });

  console.log(cart)
});
