

[

  {

    name: "fiberLookup",

    id: 10,

    fiber_lookup: {

      ref: true,

      output_ref: {

        id:9

      },

      output_crd:{

        id:9

      },

      index: "i",

      tensor: "B",

      mode:0,

      format: "compressed",

      src: true,

      root: true,

      label: "FiberLookup i: B0\ncompressed"

    }

  },

  {

    name: "fiberLookup",

    id: 11,

    fiber_lookup: {

      ref: true, 

      output_ref: {

        id: 9 

      },

      output_crd:{

        id: 9

      },

      index: "i",

      tensor: "C",

      mode: 0,

      format: "compressed",

      src: true,

      root: true,

      label: "FiberLookup i: C0\ncompressed"

    }

  },

  {

    name: "fiberwrite",

    id: 2,

    fiber_write: {

      ref: false,

      input_crd: { 

        id: 9 

      },

      index: "i",

      tensor: "X",

      mode: "0",

      format: "compressed",

      segsize: 2,

      crdsize: "B0",

      sink: true,

      label: "FiberWrite i: X0\ncompressed"

    }

  },

  {

    name: "fiberLookup",

    id: 7,

    fiber_lookup: {

      ref: true,

      output_ref: {

        id: 6

      },

      output_crd:{

        id: 6

      },

      index: "j",

      tensor: "B",

      mode: 1,

      format: "compressed",

      src: true,

      root: false,

      label: "FiberLookup j: B1\ncompressed"

    }

  },

  {

    name: "fiberLookup",

    id: 8,

    fiber_lookup: {

      ref: true,

      output_ref: {

        id: 6

      },

      output_crd:{

        id: 6

      },

      index: "j",

      tensor: "C",

      mode: 1,

      format: "compressed",

      src: true,

      root: false,

      label: "FiberLookup j: C1\ncompressed"

    }

  },

  {

    name: "fiberwrite",

    id: 1,

    fiber_write: {

      ref: false,

      input_crd: {

        id: 1 

      },

      index: "j",

      tensor: "X",

      mode: "1",

      format: "compressed",

      segsize: "B0_dim+1",

      crdsize: "B0_dim*B1_dim",

      sink: true,

      label: "FiberWrite j: X1\ncompressed"

    }

  },

  {

    name: "arrayVals",

    id: 4,

    arrayvals: {

      tensor: "B",

    }

  },

  {

    name: "arrayVals",

    id: 5,

    arrayvals: {

      tensor: "C",

    }

  },

  {

    name: "fiberwrite",

    id: 0,

    fiber_write: {

      ref: false,

      input_crd: {

        id: 1 

      },

      tensor: "X",

      mode: "vals",

      size: "1*B0_dim*B1_dim",

      sink: true,

      label: "FiberWrite Vals: X"

    }

  },

  {

    name: "union",

    id: 9,

    joiner: {

      join_type: 1,

      bundles: [

        {

        crd: 2,

        crd_label: "crd",

        ref: 0,

        }, 

        {

          crd: 0,

          ref: 7,

          ref_label: "ref_out-B"

        },

        {

          crd:0,

          ref: 8,

          ref_label: "ref-out-C"

        }

      ],

      index: "i",

      label: "union i"

    }

  },

  {

    name: "union",

    id: 6,

    joiner: {

      join_type: 1,

      bundles: [

        {

        crd: 1,

        crd_label: "crd",

        ref: 0,

        },

        {

          crd: 0,

          ref: 4,

          ref_label: "ref_out-B"

        },

        {

          crd:0,

          ref: 5,

          ref_label: "ref-out-C"

        }

      ],

      index: "j",

      label: "union j"

    }

  },

  {

    name: "add",

    id: 3,

    alu: {

      conn: {

        vals: {

          inputs: [

            { id: 4 },

            { id: 5 }

          ],

          output: { id: 0 },

        }

      },

      stages: [

        {

          inputs: [4, 5],

          output: 0,

          op: 0

        }

      ],

      output_val: 0

    }

  }

]
