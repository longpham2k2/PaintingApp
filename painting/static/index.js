function handleShowMobileMenu(){
    var mobileMenu = document.querySelector('#mobileMenu');
    var toggleBars = document.querySelector('#toggleBars');
    if(mobileMenu.classList.contains('show-mobile-menu')){
        mobileMenu.classList.remove('show-mobile-menu');
        toggleBars.innerHTML = '<i class="fa-solid fa-bars"></i>';
    } else{
        mobileMenu.classList.add('show-mobile-menu');
       toggleBars.innerHTML = '<i class="fa-solid fa-xmark closeMobileMenu"></i>'
    }
}

function scrollFeaturedList(x, y) {
    let ls = document.querySelector(".img-list");
    ls.scrollTo(ls.scrollLeft + x, ls.scrollTop + y);
}