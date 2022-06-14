<template>
    <main style="background-color:white;padding:20px">
        <a-row :gutter="[16,16]" type="flex">
            <a-col :span="24">
                <a-page-header @back="goBack" title="Pack"/>
            </a-col>
            <a-col :span="8">
                <label >
                    Nom
                    <a-input type="text" v-model="pack.name"/>
                </label>
            </a-col>
            <a-col :span="8">
                <label >
                    Durée
                    <a-input type="text" v-model.number="pack.duration" addonAfter="jours"/>
                </label>
            </a-col>
            <a-col :span="8">
                <label >
                    Montant
                    <a-input type="text" v-model.number="pack.amount" addonAfter="Fcfa" />
                </label>
            </a-col>
            <a-col :span="18">
                <label >
                    Description 
                    <a-textarea v-model="pack.description" />
                </label>
            </a-col>
            <a-col :span="24" align="end">
                <a-button type="primary" @click="validate"> Valider </a-button>
            </a-col>
        </a-row>
    </main>
</template>
<script>
import Axios from "axios";

var pack = {
    name: "",
    duration: 0,
    amount: 0,
    description:""
};

export default {
    data(){
        var editMode = this.$route.params.id ? true : false;
        return {
            pack,
            editMode
        }
    },
    beforeMount(){
        if(this.editMode){
            Axios.get("http://localhost:8000/package/"+this.$route.params.id).then(response => {
                this.pack = response.data
            })
        }
    },
    methods:{
        validate:function(){
            if(this.editMode){
                Axios.patch("http://localhost:8000/package/"+this.$route.params.id,this.pack).then(response => {
                    this.$router.go(-1)
                    this.$message.success("Package ajouté avec succès")
                })
            } else {
                Axios.post("http://localhost:8000/package/create",this.pack).then(response => {
                    this.$router.push("/package")
                }).then(response => {
                    this.$message.success("Package ajouté avec succès")
                    this.$router.go(-1)
                })
            }
        },
        goBack(){
            this.$router.go(-1)
        }
    }
}
</script>