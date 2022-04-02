paths = {"/":"home","/info":"info","/projects":"projects","/fourms":"fourms","/settings":"settings"};
current = paths[window.location.pathname];
document.getElementById(current).classList.add("active");