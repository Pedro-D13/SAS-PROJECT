// this file is shared amongst all static pages
;$(function() {
// responsive footer on static pages
$('h5.dropdown').click(function(){
   $('.mobile li').toggle([400]);
   $('.dropdown i').toggleClass('ss-navigatedown').toggleClass('ss-navigateup');
});

});


$(function() {
// business pricing page
	$('.plan').click(function(){
	   $('.select-trial').toggle([400]);
	   $('.select-trial').css({display: "none"}).css({display: "auto"});
	});
});

$(document).ready(function() {
  function filterPath(string) {
  return string
    .replace(/^\//,'')
    .replace(/(index|default).[a-zA-Z]{3,4}$/,'')
    .replace(/\/$/,'');
  }
  var locationPath = filterPath(location.pathname);
  var scrollElem = scrollableElement('html', 'body');

  $('a[href*=#]').each(function() {
    var thisPath = filterPath(this.pathname) || locationPath;

    $(this).click(function(event) {
      if(locationPath == thisPath && (location.hostname == this.hostname || !this.hostname) && this.hash.replace(/#/,'')){
        var $target = $(this.hash), target = this.hash;

        if(target && $target.offset()){
          var targetOffset = $target.offset().top;

          event.preventDefault();
          var scrollLen = $(event.target).data('scroll-length');
          $('html,body').animate({scrollTop: targetOffset}, 400, function() {
            location.hash = target;
          });
          return false;
        }
      }
    });
  });

  // use the first element that is "scrollable"
  function scrollableElement(els) {
    for (var i = 0, argLength = arguments.length; i <argLength; i++) {
      var el = arguments[i],
      $scrollElement = $(el);

      if ($scrollElement.scrollTop()> 0) {
        return el;
      }
      else {
        $scrollElement.scrollTop(1);
        var isScrollable = $scrollElement.scrollTop()> 0;
        $scrollElement.scrollTop(0);
        if (isScrollable) {
          return el;
        }
      }
    }
    return [];
  }

});

$(function() { // to show more news articles on the Press page
  $("ul.news").each(function() {
    $("a:gt(2)", this).hide(); // display the first items in the list
    $("a:nth-child(3)", this).after("<li class='more'><em>Show More...</em></li>"); // show the rest of the list items on click
  });
  $("li.more em").on("click", function() {
  	$(this).slideDown(function() {
    	var li = $(this).parents("li:first");
    	li.parent().children().show();
    	li.remove();
    	return false;
    });
  });
});

$(function() { // controls the Press Announcements dropdown menus
	$(".twotwelve").hide(function() {
		$(this).parent("li");
	});

	$("#twotwelve").click(function() {
		$(".twotwelve").toggle("li");
		$("#twotwelve i").toggleClass("ss-navigateright, ss-navigatedown");
	});

	$(".twoeleven").hide(function() {
		$(this).parent("li");
	});

	$("#twoeleven").click(function() {
		$(".twoeleven").toggle("li");
		$("#twoeleven i").toggleClass("ss-navigateright, ss-navigatedown");
	});
});

$(function() {
  $(".dropdown-toggle").toggle(".dropdown-menu");
});

$(function() {
  $(".js-nav-dropdown").click(function() {
    $(".mobile-sub-nav").toggleClass('open');
    $(this).toggleClass('ss-navigatedown').toggleClass('ss-navigateup');
  });
});

// Modal Login
$(function() {
	$('.js-sign-in').click(function(ev){
		ev.preventDefault();
		buffer.showLoginModal(ev);
		setTimeout(function(){$('div#modal-login input#email').focus()}, 500);
	});

  $('.js-sign-up').click(function(ev){
    ev.preventDefault();
    buffer.showMobileAppsModalIfNecessary(function() {
      var url = $(ev.target).attr('href');
      window.location.href = url;
    });
  });

	$('#modal-login-ajax-form').submit(function(ev){
		ev.preventDefault();
		var query_string = $('#modal-login-ajax-form').serialize();
		$.ajax({
			type: "POST",
			url: '/signin',
			data: query_string
		})
		.then(function(response){
			response = JSON.parse(response);
			if(response.success){
				if(response.success == "verify"){
					window.location = 'verify';
				}
				else{
					buffer.hideAndResetLoginModal();
					window.location.reload();
				}
			}
			else{
				window.location.reload();
			}
		});
	});

	$('li.submenu > a').click(function(ev){
		ev.preventDefault();
		var $li = $(ev.currentTarget).parent();
		var closed = !$li.hasClass('down');

		// if menu was closed then open it
		if (closed) $li.addClass('down');
	});

	$('body').click(function(ev){
		if (!ev || !$(ev.target).parents('.submenu.down').length) {
			$('.submenu.down').removeClass('down');
		}
	});

	$('.js-signup-email-have-account').click(function(ev) {
		ev.preventDefault();
		$('.js-signup-email').hide();
		$('.js-signin-full').show();
	});

	$('.js-signin-full-create-account').click(function(ev) {
    ev.preventDefault();
    buffer.showMobileAppsModalIfNecessary(function() {
      $('.js-signin-full').hide();
      $('.js-signup-email').show();
    });
  });
});

// this next block of code handles mobile sidebar toggles and overlays. when the sidebar is active,
// we push the sidebar into view and push the content out of view. clicking on the overlay will
// return the page to its original state
$(document).ready(function() {
  sidebarToggle = '#js-mobile-sidebar-toggle'
  sidebarContainer = '#js-sidebar-container'
  pagePush = '#js-sidebar-push'
  pagePushOverlay = '#js-sidebar-push-overlay'
  hero = '#js-hero'
  nav = '#js-navigation'

  // when the sidebar toggle is clicked, push the body of the page to the right and open
  // the sidebar (from offscreen left)
  $(sidebarToggle).click(function() {
    if ( !$(sidebarContainer).hasClass('is-open') ) {
      $(sidebarContainer).addClass('is-open');
      $(pagePush).addClass('is-open');
      $('body').css({'overflow':'hidden'});
    }
  });

  // when the sidebar is open, we apply an overlay to the entire page. if the user clicks anywhere
  // in this overlay, we close the sidebar and move the page content back to flush left
  $(pagePushOverlay).click(function() {
    $(sidebarContainer).removeClass('is-open')
    $(pagePush).removeClass('is-open');
    $('body').css({'overflow':'visible','zoom':'1'});
  });

  // we manually set a class on the hero to indicate whether it has a dark or light background.
  // based on what the hero color is, we can then dynamically add a class to the navigation to ensure
  // readability
  if ( $(hero).hasClass('dark-background') )
  {
    $(nav).removeClass('light-background').addClass('dark-background');
  } else {
    $(nav).addClass('light-background').removeClass('dark-background');
  }

  // for pages that have a sidebar, this bit of javascript does the magic to make it sticky as the
  // user scrolls down the page. see bufferapp.com/style-guide for reference
  if (!!$('#js-sidebar').offset()) { // make sure "#js-sidebar" element exists
    var stickyTop = $('#js-sidebar').offset().top; // returns number

    $(window).scroll(function(){ // scroll event
      var windowTop = $(window).scrollTop(); // returns number
      var splashOn = $(hero).hasClass('hero-splash');
      var offset = splashOn ? 340 : 0;

      if (stickyTop + offset < (windowTop + 30)){
        $('#js-sidebar').css({ position: 'fixed', top: 0, paddingTop: '30px' });
      } else {
        $('#js-sidebar').css({position: 'static', paddingTop: 0 });
      }
    });
  }

  var height = $(window).height();

  if ($(hero).hasClass('hero-splash')) {
    $(hero).css({'min-height':((height))+'px', 'border-bottom':'0'});
  }

  // set the height of splash heros dynamically
  $(window).resize(function() {
    var height = $(window).height();

    if ($(hero).hasClass('hero-splash')) {
      $(hero).css({'min-height':((height))+'px'});
    }
  });

  // make an entire notification clickable if that's what we want using the data-url attr.
  $('#js-clickable-notification').hover(function() {
    $(this).css({'cursor':'pointer'});
  });
  $('#js-clickable-notification').click(function() {
    window.location.href = $(this).data('url');
  });

  //
  // cards
  //

  // apply the background image to a card
  $card = document.getElementsByClassName('card');
  $.each($card, function() {
    $(this).css({'background-image':'url(' + $(this).data('card-image') + ')'});
  });

  // apply the background color to a card
  $cardColor = document.getElementsByClassName('card-color');
  $.each($cardColor, function() {
    $(this).css({'background-color': $(this).data("card-color"), 'opacity':'0.4'});
  });

  if ($('section.sidebar').length) {
    $(window).scroll(function () {
      var sidebar = $('section.sidebar');

      if ($(window).scrollTop() <= 100) {
        sidebar.css('position','').css('top','');
      }

      if (sidebar.offset().top + sidebar.height() > $("div.message-email").offset().top - 20) {
        sidebar.css('top',-(sidebar.offset().top + 20 + sidebar.height() - $("div.message-email").offset().top));
      }
    });
  }

   // Cookie consent banner

   var cookieName = 'buffer-cookie-compliance';   // Name of the cookie
   var cookieValue = 'on';                        // Value of cookie
   
   function createCookie(name,value) {
       var date = new Date();
       date.setTime(date.getTime()+(10*365*24*60*60*100)); 
       var expires = "; expires="+date.toGMTString(); 
       
       document.cookie = name+"="+value+expires+"; path=/";     
   }
 
   function showBanner() {
       var noticeBanner =  document.querySelector('.cookie-banner');
       var acceptButton = document.querySelectorAll('.accept-cookie');
       noticeBanner.classList.remove('cookie-banner--hidden');
       
       acceptButton.forEach( function(button) {
         button.addEventListener('click',function(){
           createCookie(cookieName,cookieValue);
           closeBanner(noticeBanner);
         })
       });
   }
 
   function closeBanner(banner){
     banner.classList.add('cookie-banner--hidden');  
     banner.style.display = "none"; 
   }
   
   function cookieIsSet(name,value) {
     if (document.cookie.split(';').filter(function(item) {
       return item.indexOf(name+'='+value) >= 0
     }).length) {
       return true;
     }
 
     return false;
   }
   
   // Checks to see if the cookie exists on window load
   window.onload = function(){
     if (!cookieIsSet(cookieName,cookieValue)){
       showBanner(); // If cookie doesnt exist it will display the banner
     }
   }
});
