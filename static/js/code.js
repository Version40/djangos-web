document.addEventListener('DOMContentLoaded', function() {
    var selectElement = document.getElementById('sort_select');
    selectElement.addEventListener('change', function() {
        var selectedOption = this.value;
        var url = new URL(window.location.href);
        var searchParams = new URLSearchParams(url.search);

        if (selectedOption === 'asc' || selectedOption === 'desc') {
            searchParams.set('sort', selectedOption);
        } else {
            searchParams.delete('sort');
        }

        url.search = searchParams.toString();
        window.location.href = url.toString();
    });
});

document.addEventListener('DOMContentLoaded', function() {
  var links = document.querySelectorAll('a[data-scroll-to]');

  links.forEach(function(link) {
    link.addEventListener('click', function(event) {
      event.preventDefault();

      var target = this.getAttribute('data-scroll-to');
      var targetElement = document.getElementById(target);

      if (targetElement) {
        var offset = targetElement.offsetTop;
        window.scrollTo({
          top: offset,
          behavior: 'smooth'
        });
      }
    });
  });
});


var messageOrder = document.getElementById('message_order');
if (messageOrder) {
    messageOrder.style.opacity = '1';
    messageOrder.style.visibility = 'visible';
    setTimeout(function() {
        messageOrder.style.opacity = '0';
        messageOrder.style.visibility = 'hidden';
    }, 5000); // Зникнення повідомлення після 5 секунд
}
