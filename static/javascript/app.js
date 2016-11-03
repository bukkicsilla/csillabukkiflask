'use strict';
angular.module('confusionApp', ['ui.router'])

.config(function($stateProvider) {
   $stateProvider 
   .state('app', {
         
         url:'/',
            views: {
                    'header': {
                        templateUrl : 'views/header.html'
                    },
                    'content': {
                        //template : '<h1>To be Completed</h1>',
                         templateUrl: 'views/home.html',
                        controller  : 'IndexController'
                    },
                    'footer': {
                        templateUrl: 'views/footer.html'
                      }
                }
            })

    .state({
        name: 'ok',
        url: '/ok',
        template: '<h3> ok </h3>'

    })
        // route for the aboutus page
            .state('app.aboutus', {
                url:'aboutus',
                views: {
                    'content@': {
                        templateUrl: 'views/aboutus.html' ,
                        controller  : 'AboutController'
                   }
                }
            })

      // route for the contactus page
            .state('app.contactus', {
                url:'contactus',
                views: {
                    'content@': {
                        templateUrl : 'views/contactus.html',
                        controller  : 'ContactController'
                     }
                }
            })

       // route for the menu page
            .state('app.menu', {
                url: 'menu',
                views: {
                    'content@': {
                        templateUrl : 'views/menu.html',
                        controller  : 'MenuController'
                    }
                }
            })
       // route for the dishdetail page
            .state('app.dishdetails', {
                url: 'menu/:id',
                views: {
                    'content@': {
                        templateUrl : 'views/dishdetail.html',
                        controller  : 'DishDetailController'
                   }
                }
            });
           //$urlRouterProvider.otherwise('https://ui-router.github.io/tutorial/ng1/helloworld'); 
    });
  
 $urlRouterProvider.otherwise('https://ui-router.github.io/tutorial/ng1/helloworld'); 


  
           
    



