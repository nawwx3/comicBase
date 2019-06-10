package com.grapevineindustries.comicbase

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var viewAdapter: RecyclerView.Adapter<*>
    private lateinit var viewManager: RecyclerView.LayoutManager

    val myDataset = arrayOf("nathan", "fart", "birthday")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        viewManager = LinearLayoutManager(this)
        viewAdapter = MyAdapter(myDataset)

        recyclerView = findViewById<RecyclerView>(R.id.my_recycler_view).apply {
            //use this setting to improve performance if you know that changes in content
            // do not change the layout size of the RecyclerView
            setHasFixedSize(true)

            //use a linear layout manager
            layoutManager = viewManager
            //specify a viewAdapter
            adapter = viewAdapter
        }
    }
}
