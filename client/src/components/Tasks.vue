<template>
    <div class="container">
        <div>
            <b-button @click="showModal">Add Task</b-button>
        </div>
        <div class="row">
            <div class="col-sm-10">
                <h1>Tasks</h1>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(task, index) in tasks" :key="index">
                            <td>{{ task.title }}<b-button @click="editTask(task)" variant="primary">Edit</b-button><b-button @click="removeTask(task.id)" variant="danger">Remove</b-button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <b-modal ref='add-task-modal' hide-footer title="Add Task">
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group id="input-group-1" label="Add Task" label-for="input-1">
                    <b-form-input id="input-1" v-model="form.task" type="text" required placeholder="Enter task"></b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary" @click="hideModal">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </b-modal>
        <b-modal ref='edit-task-modal' hide-footer title="Edit Task">
            <b-form @submit="onEditSubmit">
                <b-form-group id="input-group-1" label="Edit Task" label-for="input-1">
                    <b-form-input id="input-1" v-model="editedTask" type="text" required placeholder="Enter Task"></b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary" @click="hideEditModal">Submit</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            tasks: [],
            form: {
                task: '',
            },
            editedTask: '',
            editedId: ''
        }
    },
    methods: {
        getTasks() {
            const path = 'http://localhost:5000/tasks';
            axios.get(path).then((res) => {
                console.log(res)
                this.tasks = res.data.tasks;
            }).catch((error) => {
                console.error(error);
            })
        },
        removeTask(id) {
            const path = "http://localhost:5000/tasks/" + id
            axios.delete(path).then((res) => {
                this.tasks = res.data.tasks;
            }).catch((error) => {
                console.error(error);
            })
        },
        editTask(task) {
            this.$refs['edit-task-modal'].show();
            this.editedTask = task.title;
            this.editedId = task.id;
        },
        onSubmit(evt) {
            evt.preventDefault();
            const path = 'http://localhost:5000/tasks';
            let payload = {'task': this.form.task};
            console.log(payload);
            axios.post(path, payload).then((res) => {
                this.tasks = res.data.tasks;
            }).catch((error) => {
                console.error(error);
            })
        },
        onReset(evt) {
            evt.preventDefault();
            this.form.task = '';
        },
        onEditSubmit(evt) {
            evt.preventDefault();
            const path = 'http://localhost:5000/tasks/update';
            let payload = { 'id' : this.editedId, 'title': this.editedTask }
            axios.put(path, payload).then((res) => {
                this.tasks = res.data.tasks;
            }).catch((error) => {
                console.log(error);
            })
        },
        showModal() {
            this.initForm();
            this.$refs['add-task-modal'].show()
        },
        hideModal() {
            this.$refs['add-task-modal'].hide()
        },
        hideEditModal() {
            this.$refs['edit-task-modal'].hide()
        },
        initForm() {
            this.form.task = '';
        }
    },
    created() {
        this.getTasks();
    }
};
</script>