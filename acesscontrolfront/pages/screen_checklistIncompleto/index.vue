<template>

    <div class="container">
     
     <Header />
        
        <div class="content">

            <div class="row-superior">
                <TitlePage />
            </div>

            <div class="row-inferior">
            
                <div class="info-checklist">

                    <p class="title-info-checklist">Checklist Incompleto</p>

                    <p class="subject-info-checklist">Os seguintes itens estão em inconformidade:</p>

                    <p class="subtitle-info-checklist">Segurança</p>
                    <p class="data-info-checklist">Não marcados: 1,2 e 3 </p>

                    <p class="subtitle-info-checklist">Meio Ambiente</p>
                    <p class="data-info-checklist">Não marcados: 1</p> 

                </div>

                <div class="align-items-center">
                
                    <p class="p-confirm">Deseja finalizar assim mesmo e abrir ordem de chamado?</p>

                </div>

                <div class="align-items-center">
                
                    <button class="btn btn-sucess">Sim</button>
                    <button class="btn btn-alert">Não</button>

                </div>
 
            </div>

        </div>

    </div>

</template>

<script>

export default{
    name: "screen_checklistIncompleto"
}

</script>

<style lang="scss" scoped>

    @import "@/layouts/_normal_pages/Screen_ChecklistIncompleto.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";

</style>