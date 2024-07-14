console.log("hello");
let nav = false;
document.querySelector(".mob-nav-btn").addEventListener("click", function () {
  if (nav) {
    gsap.to(".mob-nav", {
      x: "100%",
    });
  } else {
    gsap.to(".mob-nav", {
      x: 0,
    });
  }
  nav = !nav;
  // console.log(nav)
});
