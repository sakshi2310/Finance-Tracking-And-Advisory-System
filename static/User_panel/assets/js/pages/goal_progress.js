'use strict';
// goal_progress.js

window.onload = function() {
     var allGoals = document.querySelectorAll('.goal-progress');
     
     allGoals.forEach(function(goal) {
         var savedAmountElement = goal.querySelector('.goal-amount[data-saved]');
         var savedAmount = parseFloat(savedAmountElement.dataset.saved);
         
         var targetAmountElement = goal.querySelector('.goal-amount[data-target]');
         var targetAmount = parseFloat(targetAmountElement.dataset.target);
         
         updateGoalProgress(goal, savedAmount, targetAmount);
     });
 }
 
 function updateGoalProgress(goal, savedAmount, targetAmount) {
     var progressBar = goal.querySelector('.progress');
 
     var progress = (savedAmount / targetAmount) * 100;
     progressBar.style.width = progress + '%';
 }
 