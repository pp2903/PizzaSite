$(document).ready(() => {
  //page loads with fading animation
  // $('body').css('display', 'none');
  // $('body').fadeIn(2000);

  //GLOBAL VARIABLES
  var cart_storage = JSON.parse(localStorage.getItem("cart"));
  var cart_items_json = document.getElementById("cart_items_json");
  var cart = []; //global variable that stores the cart value that is sent to the server

  for (i in cart_storage) {
    if (cart_storage[i] === 1) {
      cart.push(i);
    }
  }

  for (i in cart) {
  }

  //FUNCTIONS TO LOAD ON FIRST RENDER
  cart_items_json.value = JSON.stringify(cart);

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

  if (cart === null) {
    localStorage.setItem("cart", JSON.stringify({}));
  }
  //adding item to cart
  var addToCart = (id) => {
    if (localStorage.getItem("cart")) {
      var cart = JSON.parse(localStorage.getItem("cart"));
      cart[id] = 1;
      localStorage.setItem("cart", JSON.stringify(cart));
    } else {
      var cart = {};
      cart[id] = 1;
      console.log(cart);
      localStorage.setItem("cart", JSON.stringify(cart));
    }
  };

  //removing item from cart
  var removeProd = (id) => {
    var cart = JSON.parse(localStorage.getItem("cart"));

    cart[id] = 0;
    console.log(cart);
    localStorage.setItem(JSON.stringify(cart));
  };

  //functions that change the state of the buttons based on items in local storage

  // adding product cart
  $(".buy-btn").on("click", function () {
    var btn_id = $(this).attr("id");
    addToCart(btn_id);

    //adding styles on buy-button click
    $(this).text("Added");
    $(this).parent().children(".remove-btn").css("display", "inline");
    // Add a class to change the button color
    $(this).removeClass("btn-success-light");
    $(this).addClass("btn-success");
    $(this).addClass("added");
    //updating the cart
    cart.push(btn_id);
    cart_items_json.value = JSON.stringify(cart);
  });

  $(".remove-btn").on("click", function () {
    var btn_id = $(this).parent().children(".buy-btn").attr("id");
    $(this).parent().children(".buy-btn").text("Add to cart");
    $(this).parent().children(".buy-btn").removeClass("btn-success");
    $(this).parent().children(".buy-btn").addClass("btn-success-light");

    $(this).css("display", "none");
    console.log($(this).parent().children(".buy-btn").attr("id"));
    var prod_id = $(this).parent().children(".buy-btn").attr("id");

    var cart_local = JSON.parse(localStorage.getItem("cart"));
    delete cart_local[prod_id];
    localStorage.setItem("cart", JSON.stringify(cart_local));

    // updating the cart
    cart.pop(btn_id);
    cart_items_json.value = JSON.stringify(cart);
  });

  var order = [];

  if (cart !== null) {
    for (var i in cart) {
      var obj = {
        id: i,
        qty: 1,
      };
      order.push(obj);
    }
  }

  //change the state of the elements when cart page loads, based on the added items.

  for (i in cart_storage) {
    if (cart_storage[i] === 1) {
      $("#" + i).click();
      
    }
  }

  // clear cart button

  $("#clear-cart-btn").click(() => {
    localStorage.setItem("cart", JSON.stringify({}));
    cart = [];
    cart_items_json.value = JSON.stringify(cart);
    var cart_button = $("#cart-btn").click();
  });

  // remove button on the cart page
  $(".rmv-btn").on("click", function () {
    // Get the parent element and set its display property to none
    $(this).parent().parent().css("display", "none");
    var prod_id = $(this).attr("id");
    let id = prod_id.charAt(prod_id.length - 1);

    cart.pop("pr" + id);
    cart_items_json.value = JSON.stringify(cart);

    //updating local storage

    let cart_loc = JSON.parse(localStorage.getItem("cart"));

    delete cart_loc["pr" + id];

    localStorage.setItem("cart", JSON.stringify(cart_loc));
    if (Object.keys(cart_loc).length == 0) {
      $("#cart-btn").click();
    }
    console.log(cart_loc);
  });

  console.log(cart)
  console.log(cart_storage)
  console.log(cart_items_json.value)


  //order array that is initialized only when we go to the cart
  let order_arr = []
  

  
  


});
