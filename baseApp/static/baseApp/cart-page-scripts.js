$(document).ready(function () {
  //cart item quantity select button



  $("#order_items_json").val(localStorage.getItem("cartItems"))

  $(".cart-item-qty").change(function () {
    // Get the selected value
    let id = $(this).attr("id").substring(10);
    let cartItems = JSON.parse(localStorage.getItem("cartItems"));
    let new_price = 0;
    let total_price = 0;
    for (var i in cartItems) {
      if (cartItems[i].id === parseInt(id)) {
        cartItems[i].qty = $(this).val();

        new_price = cartItems[i].qty * cartItems[i].price;
      }
      total_price = total_price + cartItems[i].qty * cartItems[i].price;
    }
    localStorage.setItem("cartItems", JSON.stringify(cartItems));
    //setting the new price for each item on cart page
    $(this).parent().parent().children().eq(2)[0].innerText = "$" + new_price;

    //changing the total amount on the page
    $("#total-price-cart")[0].innerText = "$ " + total_price;


    //changing the value of order_items_json
    $("#order_items_json").val(localStorage.getItem("cartItems"))

    
  });

  //clicking remove on the cart
  $(".rmv-btn").click(function () {

    var id = $(this).attr("id").substring(8);

    var cartItems = JSON.parse(localStorage.getItem("cartItems"));
    var cart = JSON.parse(localStorage.getItem("cart"));

    //removing from cart object

    delete cart["pr" + id];

    localStorage.setItem("cart", JSON.stringify(cart));

    //setting the value of the cart_item_json
    $("#cart_items_json").val(JSON.stringify(cart));
    
    $("#cart-btn").click();

    //remove it from the cartItem array

    cartItems = cartItems.filter((item) => {
      if (item.id !== parseInt(id)) {
        return item;
      }
    });

    localStorage.setItem("cartItems", JSON.stringify(cartItems));

    //changing the value of order_items_json
    $("#order_items_json").val(localStorage.getItem("cartItems"))

    if (cartItems.length === 0) {
      localStorage.removeItem("cartItems");
      //   $("#clear-cart-btn").click();
    }

    
  });

  //clear cart functionality
  $("#clear-cart-btn").click(() => {
    let cartItems = JSON.parse(localStorage.getItem("cartItems"));
    let cart = JSON.parse(localStorage.getItem("cart"));

    cart = {};
    cartItems = [];

    localStorage.setItem("cart", JSON.stringify(cart));
    localStorage.setItem("cartItems", JSON.stringify(cartItems));

    let cart_item_json = $("#cart_items_json");
    cart_item_json.val(JSON.stringify({}));
    $("#order_items_json").val(JSON.stringify([]));
    $("#cart-btn").click();
  });

 


  // function to call when leaving the page
  function handleBeforeUnload() {
    // Delete the item from local storage
    localStorage.removeItem("cartItems");
  }
  
  // Attach the function to the beforeunload event
  window.addEventListener("beforeunload", handleBeforeUnload);
});
