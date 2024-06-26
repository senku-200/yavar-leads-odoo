document.querySelectorAll('td').forEach(function(td) {
    var timer;
    var startX, startY;

    td.addEventListener('touchstart', function(event) {
        // Store the starting touch position
        var touch = event.touches[0];
        startX = touch.clientX;
        startY = touch.clientY;

        clearTimeout(timer);

        timer = setTimeout(function() {
            document.querySelectorAll('.tooltip-mobile').forEach(function(tooltip) {
                tooltip.remove();
            });

            var tooltip = td.querySelector('.tooltip-mobile');
            if (!tooltip) {
                tooltip = document.createElement('div');
                tooltip.className = 'tooltip-mobile';
                tooltip.textContent = td.getAttribute('title');
                td.appendChild(tooltip);
            }
            
            // Automatically remove the tooltip after 3 seconds
            setTimeout(function() {
                tooltip.remove();
            }, 3000);
        }, 500);
    });

    td.addEventListener('touchmove', function(event) {
        var touch = event.touches[0];
        var deltaX = Math.abs(touch.clientX - startX);
        var deltaY = Math.abs(touch.clientY - startY);

        // If the touch moves beyond a threshold, cancel the tooltip
        if (deltaX > 10 || deltaY > 10) {
            clearTimeout(timer);
        }
    });

    td.addEventListener('touchend', function() {
        clearTimeout(timer);
    });

    td.addEventListener('touchcancel', function() {
        clearTimeout(timer);
    });
});
