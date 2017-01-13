/* the best one can do to try to make a function inline */
#if defined(_MSC_VER)
#  define FORCE_INLINE    __forceinline
#else
#  define FORCE_INLINE inline __attribute__((always_inline))
#endif
