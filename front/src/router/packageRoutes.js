export const PackageRoute = [
    {
		path: '/package',
		name: 'Packs',
		layout: "dashboard",
		component: () => import('../views/package/PackageView.vue'),
	},
	{
		path: '/package/detail/:id',
		name: 'Detail Pack',
		layout: "dashboard",
		component: () => import('../views/package/PackageDetailView.vue'),
	},
	{
		path: '/package/new',
		name: 'Nouveau Pack',
		layout: "dashboard",
		component: () => import('../views/package/PackageDetailView.vue'),
	},
]