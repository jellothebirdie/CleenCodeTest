const trashItems = document.querySelectorAll('.trash');

trashItems.forEach(item => {

    const pageHeight = document.documentElement.scrollHeight;

    // Vertical limits
    const minY = 150;                   // keep away from top
    const maxY = pageHeight - 50;       // bottom of scrollable page

    // ⭐ Random starting position
    let x = Math.random() * (window.innerWidth - 50);
    let y = Math.random() * (maxY - minY) + minY;

    // ⭐ Random velocity
    let vx = (Math.random() * 4) - 2; 
    let vy = (Math.random() * 4) - 2;

    // ⭐ Random rotation + spin speed
    let rotation = Math.random() * 360;
    let rotationSpeed = (Math.random() * 4) - 2;

    function animate() {
        x += vx;
        y += vy;

        // bounce off left/right
        if (x <= 0 || x >= window.innerWidth - 50) vx = -vx;

        // bounce off min/max Y
        if (y <= minY || y >= maxY) vy = -vy;

        // clamp vertical position
        y = Math.max(minY, Math.min(maxY, y));

        // rotate item
        rotation += rotationSpeed;

        // apply position + rotation
        item.style.left = x + 'px';
        item.style.top = y + 'px';
        item.style.transform = `rotate(${rotation}deg)`;

        requestAnimationFrame(animate);
    }

    animate();
});
