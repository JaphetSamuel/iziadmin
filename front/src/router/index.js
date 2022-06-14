import Vue from 'vue'
import VueRouter from 'vue-router'
import {PackageRoute} from './packageRoutes'

Vue.use(VueRouter)

let routes = [
	{
		// will match everything
		path: '*',
		component: () => import('../views/404.vue'),
	},
	{
		path: '/',
		name: 'Home',
		redirect: '/dashboard',
	},
	{
		path: '/dashboard',
		name: 'Dashboard',
		layout: "dashboard",
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () => import(/* webpackChunkName: "dashboard" */ '../views/Dashboard.vue'),
	},
	{
		path: '/layout',
		name: 'Layout',
		layout: "dashboard",
		component: () => import('../views/Layout.vue'),
	},
	{
		path: '/tables',
		name: 'Tables',
		layout: "dashboard",
		component: () => import('../views/Tables.vue'),
	},
	{
		path: '/driver',
		name: 'Gestion des conducteurs',
		layout: "dashboard",
		component: () => import('../views/DriverView.vue'),
	},
	{
		path: '/driver/:id',
		name: 'Profil Conducteur',
		layout: "dashboard",
		component: () => import('../components/Driver/DriverColumn.vue'),
	},
	{
		path: '/map',
		name: 'Carte',
		layout: "dashboard",
		component: () => import('../views/MapView.vue'),
	},
	{
		path: '/order',
		name: 'Commande',
		layout: "dashboard",
		component: () => import('../views/OrderView.vue'),
	},
	{
		path: '/order/:id',
		name: 'Detail de la commande',
		layout: "dashboard",
		component: () => import('../views/OrderDetailView.vue'),
	},
	{
		path: '/billing',
		name: 'Billing',
		layout: "dashboard",
		component: () => import('../views/Billing.vue'),
	},
	{
		path: '/promotion',
		name: 'Promotion',
		layout: "dashboard",
		component: () => import('../views/PromotionView.vue'),
	},
	{
		path: '/promotion_detail/:id',
		name: 'Detail Promotion',
		layout: "dashboard",
		component: () => import('../views/PromotionDetailView.vue'),
	},
	{
		path: '/pricing',
		name: 'Gestion des prix',
		layout: "dashboard",
		component: () => import('../views/PricingView.vue'),
	},
	{
		path: '/pricing/detail/:id',
		name: 'Detail Prix',
		layout: "dashboard",
		component: () => import('../views/PricingDetailView.vue'),
	},
	{
		path: '/pricing/new',
		name: 'Nouveau Prix',
		layout: "dashboard",
		component: () => import('../views/PricingDetailView.vue'),
	},
	{
		path: '/Profile',
		name: 'Profile',
		layout: "dashboard",
		meta: {
			layoutClass: 'layout-profile',
		},
		component: () => import('../views/Profile.vue'),
	},
	{
		path: '/sign-in',
		name: 'Sign-In',
		component: () => import('../views/Sign-In.vue'),
	},
	{
		path: '/sign-up',
		name: 'Sign-Up',
		meta: {
			layoutClass: 'layout-sign-up',
		},
		component: () => import('../views/Sign-Up.vue'),
	},
	...PackageRoute
]

// Adding layout property from each route to the meta
// object so it can be accessed later.
function addLayoutToRoute( route, parentLayout = "default" )
{
	route.meta = route.meta || {} ;
	route.meta.layout = route.layout || parentLayout ;
	
	if( route.children )
	{
		route.children = route.children.map( ( childRoute ) => addLayoutToRoute( childRoute, route.meta.layout ) ) ;
	}
	return route ;
}

routes = routes.map( ( route ) => addLayoutToRoute( route ) ) ;

const router = new VueRouter({
	mode: 'hash',
	base: process.env.BASE_URL,
	routes,
	scrollBehavior (to, from, savedPosition) {
		if ( to.hash ) {
			return {
				selector: to.hash,
				behavior: 'smooth',
			}
		}
		return {
			x: 0,
			y: 0,
			behavior: 'smooth',
		}
	}
})

export default router
