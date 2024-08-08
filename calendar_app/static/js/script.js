document.addEventListener("DOMContentLoaded", function() {
  const selectedDay = document.getElementById("day").value;
  if (selectedDay) {
    document.querySelectorAll(".calendar td").forEach(function(td) {
      if (td.innerHTML.trim() === selectedDay) {
        td.classList.add("selected-day");
      }
    });
  }
  document.querySelectorAll(".calendar td").forEach(function(td) {
    if (td.innerHTML.trim() !== "" && !isNaN(td.innerHTML.trim())) {
      td.style.cursor = "pointer";
      td.addEventListener("click", function() {
        document.getElementById("day").value = this.innerHTML.trim();
        document.querySelectorAll(".calendar td.selected-day").forEach(function(day) {
          day.classList.remove("selected-day");
        });
        this.classList.add("selected-day");
        document.getElementById("calendar-form").submit();
      });
    }
  });
  document.querySelectorAll(".delete-task-btn").forEach(function(btn) {
    btn.addEventListener("click", function() {
      this.closest("form").submit();
    });
  });
});