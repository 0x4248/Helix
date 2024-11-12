
document.querySelectorAll('a').forEach(a => {
	a.addEventListener('click', () => {
		document.getElementById('main').classList.add('animation-out-main');
	});
});