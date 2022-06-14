<!-- 
	This is the tables page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
	<div>

		<!-- Authors Table -->
		<a-row :gutter="24" type="flex">

			<!-- Authors Table Column -->
			<a-col :span="24" class="mb-24">
				<driver-table/>
			</a-col>
			<!-- / Authors Table Column -->
		</a-row>
		<!-- / Authors Table -->

	</div>
</template>

<script>

	// "Authors" table component.
	import CardAuthorTable from '../components/Cards/CardAuthorTable' ;
	import DriverTable from '../components/Driver/DriverTable.vue';


	var columns = [
    {
        title:"id",
        key:"ID",
        dataIndex:"id"
    },
    {
        title:"Nom complet",
        key:"fullname",
        dataIndex:"fullname"
    },
    {
        title:"Email",
        key:"email",
        dataIndex:"email"
    },
    {
        title:"Telephone",
        key:"contact",
        dataIndex:"contact"
    },
    {
        title:"en ligne",
        key:"isonline",
        dataIndex:"is_online"
    },
    {
        title:"",
        key:"action",
        dataIndex:"action"
    }
]
	

	export default ({
		components: {
			CardAuthorTable,
			DriverTable
		},
		data() {
			return {

				// Associating "Authors" table columns with its corresponding property.
				table1Columns: columns,
			}
		},
		computed: {
			table1Data() {
				var table = []
				Axios.get("https://stormy-tor-92609.herokuapp.com/driver/driver").then(response => {
					table =  response.data;
				});

				return table;
			},
		},
	})

</script>

<style lang="scss">
</style>