<template>
    <main style="background-color:white">
        <a-row>
            <a-col :span="24">
                <a-page-header title="Service">
                    <template #extra>
                            <a-button>
                                <a-icon type="plus" />
                                <router-link to="/pricing/new">
                                    Ajouter
                                </router-link>
                            </a-button>
                    </template>
                </a-page-header>
            </a-col>
            <a-col :span="24">
                <a-table :data-source="services" :columns="service_columns" rowKey="id">
                    <span slot="action" slot-scope="action">
                        <router-link :to="'/pricing/detail/'+action.id" type="primary" >
                            <a-icon type="edit" />
                            Modifier
                        </router-link>  
                        <a-button type="danger" @click="deleteService(action.id)">
                            <a-icon type="delete" />
                            Supprimer
                        </a-button>
                    </span>
                </a-table>
            </a-col>
        </a-row>
    </main>
</template>
<script>
import Axios from 'axios'

const service_columns =[
    {
        key:"name",
        title:"Nom",
        dataIndex:"name",
        scopedSlots:{customRender:"name"}
    },
    {
        key:"categorie",
        title:"Catégorie",
        dataIndex:"categorie_id",
        scopedSlots:{customRender:"categorie"}
    },
    {
        key:"description",
        title:"Description",
        dataIndex:"description",
        scopedSlots:{customRender:"name"}
    },
    {
        key:"action",
        title:"Action",
        scopedSlots:{customRender:"action"}
    }
] 

export default{
    data(){

        return{
            services:[],
            service_columns
        }
    },
    methods:{
        deleteService:function(id){
            Axios.delete("http://localhost:8000/service/delete/"+id,).then((response)=>{
                this.services = response.data
            }).then(()=>{
                this.$message.success("Service supprimé avec succès")
            }).catch((error)=>{
                this.$message.error("Erreur lors de la suppression du service")
            })
        }
    },
    beforeCreate() {
        Axios.get("http://localhost:8000/service/all").then(response => {
            this.services = response.data
        })
    },
}
</script>