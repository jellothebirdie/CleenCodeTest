const trashItems = document.querySelectorAll('.trash');

trashItems.forEach(item => {
// Random starting position
let x = Math.random() * (window.innerWidth - 50);
let y = Math.random() * (window.innerHeight - 50);

// Random velocity
let vx = (Math.random() * 4) - 2; // horizontal speed
let vy = (Math.random() * 4) - 2; // vertical speed

// Random rotation speed (degrees per frame)
let rotation = Math.random() * 360; // starting rotation
let rotationSpeed = (Math.random() * 4) - 2; // can rotate clockwise or counterclockwise

function animate() {
x += vx;
y += vy;

// bounce off edges
if (x <= 0 || x >= window.innerWidth - 50) vx *= -1;
if (y <= 0 || y >= window.innerHeight - 50) vy *= -1;

// update rotation
rotation += rotationSpeed;

// apply transform
item.style.left = x + 'px';
item.style.top = y + 'px';
item.style.transform = `rotate(${rotation}deg)`;

requestAnimationFrame(animate);
}

animate();
});