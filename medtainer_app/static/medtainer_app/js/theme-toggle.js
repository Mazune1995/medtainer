// Load saved theme
let theme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', theme);

const toggle = document.getElementById('theme-toggle');
toggle.checked = theme === 'dark';

function toggleTheme() {
    theme = (theme === 'light') ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

toggle.addEventListener('change', toggleTheme);