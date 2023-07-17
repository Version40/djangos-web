function OpenAuth() {
    const auth = document.getElementById('auth_main_block')
    auth.style.visibility = 'visible';
    auth.style.opacity = '1';

    const reg = document.getElementById('reg_main_block')
    reg.style.visibility = 'hidden';
    reg.style.opacity = '0';
}

document.getElementById('cancel_button').addEventListener('click', function (e) {
    const auth = document.getElementById('auth_main_block');
    auth.style.visibility = 'hidden';
    auth.style.opacity = '0';
});

window.addEventListener('load', function() {
    const errorDiv = document.querySelector('.form-errors');
    if (errorDiv && errorDiv.children.length > 0) {
        const auth = document.getElementById('auth_main_block');
        auth.style.visibility = 'visible';
        auth.style.opacity = '1';
        auth.style.transition = 'all 0s easy';
    }

    const errorDivReg = document.querySelector('.form-errors-reg');
    if (errorDivReg && errorDivReg.children.length > 0) {
        const reg = document.getElementById('reg_main_block');
        reg.style.visibility = 'visible';
        reg.style.opacity = '1';
        reg.style.transition = 'all 0s easy';
    }
});

document.getElementById('cancel_button').addEventListener('click', function (e) {
    const auth = document.getElementById('auth_main_block')
    auth.style.visibility = 'hidden';
    auth.style.opacity = '0';
})

document.getElementById('register_link').addEventListener('click', function (e) {
    const auth = document.getElementById('auth_main_block')
    auth.style.visibility = 'hidden';
    auth.style.opacity = '0';

    const reg = document.getElementById('reg_main_block')
    reg.style.visibility = 'visible';
    reg.style.opacity = '1';
})

document.getElementById('cancel_reg_button').addEventListener('click', function (e) {
    const reg = document.getElementById('reg_main_block')
    reg.style.visibility = 'hidden';
    reg.style.opacity = '0';
})


const el = document.getElementById('user_menu_block')
if (el) {
    el.addEventListener('mouseover', function (e) {
    const hidden = document.getElementById('hidden_user_menu')
    hidden.style.visibility = 'visible';
    hidden.style.opacity = '1';
    hidden.style.transition = 'all .5s easy';

    const visible_menu = document.getElementById('user_menu_block')
    visible_menu.style.width = '200px'
    visible_menu.style.background = 'rgb(34, 34, 34)'
    visible_menu.style.borderLeft = '1px solid grey'
    visible_menu.style.borderRight = '1px solid grey'
    visible_menu.style.borderTop = '1px solid grey'
    visible_menu.style.borderRadius = '10px 10px 0 0'
})
    el.addEventListener('mouseout', function (e) {
    const hidden = document.getElementById('hidden_user_menu')
    hidden.style.visibility = 'hidden';
    hidden.style.opacity = '0';
    hidden.style.transition = 'all 0s easy';

    const visible_menu = document.getElementById('user_menu_block')
    visible_menu.style.width = 'auto'
    visible_menu.style.background = 'transparent'
    visible_menu.style.borderLeft = 'none'
    visible_menu.style.borderRight = 'none'
    visible_menu.style.borderTop = 'none'
    visible_menu.style.borderRadius = '0'
})
}

const header = document.getElementById('main_header')
window.addEventListener('scroll', function() {
  if (window.scrollY >= 90) {
    header.style.zIndex = '999'
  } else {
    header.style.zIndex = '0'
  }
});
